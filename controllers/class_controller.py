from models.class_model import ClassModel

class ClassController:
    def __init__(self, view):
        self.model = ClassModel()
        self.view = view
        self.view.set_controller(self)

    def load_classes(self):
        data = self.model.get_all_classes()
        self.view.display_classes(data)

    def add_class(self, malop, tenlop, giangvien):
        self.model.add_class(malop, tenlop, giangvien)
        self.load_classes()

    def update_class(self, malop, tenlop, giangvien):
        self.model.update_class(malop, tenlop, giangvien)
        self.load_classes()

    def delete_class(self, malop):
        self.model.delete_class(malop)
        self.load_classes()
