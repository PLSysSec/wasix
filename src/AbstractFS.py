class File:
    def __init__(self,
            name = None,
            mode = None,
            linked_file = None,
            is_dir = False,
            is_base = False):
        self.name = name
        self.mode = mode
        self.is_symlink = True if linked_file else False;
        self.linked_file = linked_file;
        self.is_dir = is_dir;
        self.children = [] if self.is_dir else None
        self.is_base = is_base
        self.parent = None

    def rename(self, new_name):
        self.name = new_name

    def create_symlink(self, link_name):
        return File(name=link_name, file=self, is_dir=self.is_dir);

    def add_file(self, file):
        if(self.is_dir):
            self.children.append(file);
            file.parent = self
        else: print("{} is not a dir".format(self.name))
    
    def add_files(self, files):
        for file in files: self.add_file(file)
    
    def remove_file(self, file):
        if(self.is_dir):
            self.children.remove(file);
            file.parent = None
        else: print("{} is not a dir".format(self.name))
    
    def get_path(self):
        if(self.is_base):
            return self.name
        else:
            return "{}/{}".format(self.parent.get_path(), self.name)

    def __str__(self):
        return self.get_path()

class Dir(File):
    def __init__(self, name=None, children=[], mode=None):
        super.__init__(self, name=name, mode=mode, is_dir=True)
        for file in children:
            self.add_file(file)


class TestDirectory:
    def __init__(self, files):
        self.files = files
    def create(self, base):
        td = File(base, 777, is_dir=True, is_base=True)
        td.add_files(self.files)
        return td

def walk_through(file):
    if(file.is_dir):
        ret = [file]
        for ch in file.children:
            ret += walk_through(ch)
        return ret
    else: return [file]