workflow "Build" {
  on = "push"
  resolves = ["Build Package"]
}

action "Build Package" {
  uses = "python"
  runs = "python setup.py sdist bdist_wheel"
}
