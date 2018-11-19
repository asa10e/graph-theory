from Page import Page

class Book(object):

    def __init__(self, pages = set()):

        assert len(set([p.spine for p in pages])) == 1, 'All pages must have identical spines'

        self.pages = pages
        self.spine = next(iter(pages)).spine


    def is_nice_embedding(self):
        """
        True if each page of the book has no intersections
        False otherwise
        """
        for p in self.pages:
            if p.has_intersections() == True:
                return False
        return True
