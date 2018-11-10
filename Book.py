from Page import Page

class Book(object):

    def __init__(self, pages = set()):

        if len(set([p.spine for p in pages])) == 1:
            self.spine = spine
            self.pages = pages
        else:
            print('Pages must have identical spines!')

    def is_nice_embedding(self):
        """
        True if each page of the book has no intersections
        False otherwise
        """
        for p in self.pages:
            if p.has_intersections() == True:
                return False
        return True
