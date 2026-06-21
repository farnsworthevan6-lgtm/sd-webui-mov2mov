import launch

requirements = [
    ("cv2", "opencv-python"),
    ("imageio", "imageio"),
    ("imageio_ffmpeg", "imageio-ffmpeg"),
]

missing = [pkg for modulename, pkg in requirements if not launch.is_installed(modulename)]
if missing:
    print('Installing requirements for Mov2mov: %s' % ', '.join(missing))
    for package in missing:
        launch.run_pip(f"install {package}", "requirements for Mov2mov")
