from file import File
from folder import Folder

if __name__ == "__main__":
    computer = Folder("Computer")
    documents = Folder("Documents")
    photos = Folder("Photos")
    university = Folder("University")

    resume = File("resume.pdf")
    homework = File("homework.docx")
    java_file = File("Java.java")
    python_file = File("Python.py")
    photo1 = File("photo1.jpg")
    photo2 = File("photo2.jpg")
    music = File("music.mp3")

    university.add(java_file)
    university.add(python_file)

    documents.add(resume)
    documents.add(homework)
    documents.add(university)

    photos.add(photo1)
    photos.add(photo2)

    computer.add(documents)
    computer.add(photos)
    computer.add(music)

    computer.show()