workflow "Publish to PyPi" {
  resolves = ["Publish Python Package"]
  on = "push"
}

action "Publish Python Package" {
  uses = "mariamrf/py-package-publish-action@v0.0.2"
}
