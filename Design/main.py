from file import File
from folder import Folder

if __name__ == "__main__":
    computer = Folder("Computer")
    documents = Folder("Documents")
    photos = Folder("Photos")

    resume = File("resume.pdf")
    homework = File("homework.docx")
    photo1 = File("photo1.jpg")
    photo2 = File("photo2.jpg")
    music = File("music.mp3")

    documents.add(resume)
    documents.add(homework)

    photos.add(photo1)
    photos.add(photo2)

    computer.add(documents)
    computer.add(photos)
    computer.add(music)

    computer.show()