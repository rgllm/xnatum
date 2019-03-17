# XNATYPY: https://xnat.readthedocs.io/en/latest/
import xnat as xnatpy
import os, sys
from .util import tmp_zip

# Main interface with XNAT
# methods created to simplify XNAT access
class Xnat:
    def __init__(self, server, user, password):
        self.server   = server
        self.user     = user
        self.password = password
        self.__prearc_session = None
        self.__connect()

    # Uses interface from xnatpy
    def __connect(self):
        self.session = xnatpy.connect(self.server, user=self.user, password=self.password)

    # Listing all projects
    def list_projects(self):
        projects = []
        for project in self.session.projects.values():
            projects.append( (project.id, project.name) )
        return projects
    
    def get_sessions(self, lproject, lsubject):
        project = self.session.projects[lproject]
        subject = project.subjects[lsubject]
        session = [x.label for x in subject.experiments.values()]
        return session
        
    # Function to import resources
    def import_resource( self, obj, subdir, files ):
        for file in files:
            filename = os.path.basename(file)
            uri = '{}/resources/{}/files/{}'.format(obj.uri, subdir, filename)
            self.session.put(uri, files={'file': open(file, 'rb')})

    # function to send a specific sequence to xnat
    def send_sequence(self, project, subject, sequence_dir, session = '', destination='/prearchive'):
        zipfname = tmp_zip( sequence_dir )
        try:
            self.__prearc_session = self.session.services.import_( zipfname,\
                overwrite='append',\
                project=project,\
                subject=subject,\
                experiment=subject+'_'+session,\
                destination=destination,\
                trigger_pipelines=False )
        except:
            print("Unexpected error during XNAT import:")
            print(sys.exc_info())
        os.remove( zipfname )

    # function to send a complete session to xnat
    def send_session(self, project, subject, session_dir, sequences = None, session = ''):
        if not sequences:
            sequences = os.listdir(session_dir)

        dest = '/prearchive'
        for (n, sequence) in enumerate(sequences):
            print("[{:02d}] Sending: {}".format(n+1, sequence))
            sequence_dir = os.path.join(session_dir, sequence)
            self.send_sequence( project, subject, sequence_dir, session=session, destination=dest )
            dest = self.__prearc_session.uri
        
        self.__prearc_session.archive()
        self.__prearc_session = None

        print('Finished!')
    