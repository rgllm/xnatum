# XNATYPY: https://xnat.readthedocs.io/en/latest/
import xnat as xnatpy
import os
import sys
from .util import tmp_zip
import dicom2nifti
import shutil

# Main interface with XNAT
# methods created to simplify XNAT access


class Xnat:
    def __init__(self, server, user, password):
        self.server = server
        self.user = user
        self.password = password
        self.__prearc_session = None
        self.__connect()

    # Uses interface from xnatpy
    def __connect(self):
        self.session = xnatpy.connect(
            self.server, user=self.user, password=self.password)

    # Listing all projects
    def list_projects(self):
        projects = []
        for project in self.session.projects.values():
            projects.append((project.id, project.name))
        return projects

    # download train and test data
    def download_dp_data(self, lproject):
        project = self.session.projects[lproject]
        train_dir = os.path.expanduser(lproject + '/TRAIN')
        test_dir = os.path.expanduser(lproject + '/TEST')

        if not os.path.exists(train_dir):
            os.makedirs(train_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
        for subject in project.subjects.values():
            for experiment in subject.experiments.values():
                print("Downloading ", experiment)
                # Validate this experiment.label
                if(experiment.label.find('TRAIN') != -1):
                    experiment.download_dir(train_dir)
                else:
                    experiment.download_dir(test_dir)
        return[train_dir, test_dir]

    def get_train_data(self, lproject):
        project = self.session.projects[lproject]
        trainData = []
        for subject in project.subjects.values():
            for experiment in subject.experiments.values():
                if(experiment.label.find('TRAIN') != -1):
                    trainData.append(experiment)
        return trainData

    def get_test_data(self, lproject):
        project = self.session.projects[lproject]
        testData = []
        for subject in project.subjects.values():
            for experiment in subject.experiments.values():
                if(experiment.label.find('TEST') != -1):
                    testData.append(experiment)
        return testData

    # Download subject sessions to a local folder
    def download_subject_sessions(self, lproject, lsubject):
        project = self.session.projects[lproject]
        subject = project.subjects[lsubject]
        download_dir = os.path.expanduser(lproject)
        print('Using {} as download directory'.format(download_dir))
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        source = os.path.join('.', download_dir)
        for experiment in subject.experiments.values():
            print("Downloading ", experiment)
            experiment.download_dir(download_dir)
        session = [x.label for x in subject.experiments.values()]
        return session

    # Returns a subject sessions without the need to downlaod them locally
    def get_subject_sessions(self, lproject, lsubject):
        project = self.session.projects[lproject]
        subject = project.subjects[lsubject]
        return subject.experiments.values()

    # Download all sessions from a project
    def download_project_sessions(self, lproject):
        project = self.session.projects[lproject]
        download_dir = os.path.expanduser(lproject)
        print('Using {} as download directory'.format(download_dir))
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        for subject in project.subjects.values():
            for experiment in subject.experiments.values():
                print("Downloading ", experiment)
                experiment.download_dir(download_dir)
        return download_dir

    # Returns all the sessions from a project without the need to downlaod them locally
    def get_project_sessions(self, lproject):
        project = self.session.projects[lproject]
        allexperiments = []
        for subject in project.subjects.values():
            for experiment in subject.experiments.values():
                allexperiments.append(experiment)
        return allexperiments

    # Converts Dicom to Nifti files
    def convert_dicom_nifti(self, dicom_directory, output_folder):
        dicom2nifti.convert_directory(
            dicom_directory, output_folder, compression=True, reorient=True)

    # Function to import resources
    def import_resource(self, obj, subdir, files):
        for file in files:
            filename = os.path.basename(file)
            uri = '{}/resources/{}/files/{}'.format(obj.uri, subdir, filename)
            self.session.put(uri, files={'file': open(file, 'rb')})

    # function to send a specific sequence to xnat
    def send_sequence(self, project, subject, sequence_dir, session='', destination='/prearchive'):
        zipfname = tmp_zip(sequence_dir)
        try:
            self.__prearc_session = self.session.services.import_(zipfname,
                                                                  overwrite='append',
                                                                  project=project,
                                                                  subject=subject,
                                                                  experiment=subject+'_'+session,
                                                                  destination=destination,
                                                                  trigger_pipelines=False)
        except:
            print("Unexpected error during XNAT import:")
            print(sys.exc_info())
        os.remove(zipfname)

    # function to send a complete session to xnat
    def send_session(self, project, subject, session_dir, sequences=None, session=''):
        if not sequences:
            sequences = os.listdir(session_dir)

        dest = '/prearchive'
        for (n, sequence) in enumerate(sequences):
            print("[{:02d}] Sending: {}".format(n+1, sequence))
            sequence_dir = os.path.join(session_dir, sequence)
            self.send_sequence(project, subject, sequence_dir,
                               session=session, destination=dest)
            dest = self.__prearc_session.uri

        self.__prearc_session.archive()
        self.__prearc_session = None

        print('Finished!')
