from model.da.database import DataBaseManager
from model.entity.menu_item import Menu


class MenuDa(DataBaseManager):
    def find_by_text(self,word):
        self.make_engine()
        menuitem_list=self.session.query(Menu).filter(Menu.text.like(f"%{word}%"))
        self.session.close()
        return menuitem_list
