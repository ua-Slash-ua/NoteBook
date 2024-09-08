import datetime



class RecordingNote:
    def __init__(self,title:str, text:str):
        self.num = None # 0
        self.time = None # 1
        self.title = title.strip() # 2
        self.text = text # 3

    def return_title(self):
        if not self.title:
            self.title = self.text.split('\n')[0][:30]+'...'
        return self.title

    def return_text(self):
        return self.text

    def create_note(self):
        self.time = datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")
        with open('data.txt', 'r+', encoding='utf-8') as f:
            f.seek(0)
            self.num = len(f.readlines())+1
            f.write(f'{self.num})|{self.time}|{self.return_title()}|{self.return_text()}\n')

    def return_data_note(self):
        with open('data.txt', 'r+', encoding='utf-8') as f:
            data = f.readlines()
        self.num = data[-1].split('|')[0]
        self.title = data[-1].split('|')[2]
        return self.num,self.title

class ShowNotes:
    def __init__(self):
        self.info = []
        self.num_d = None
    def return_all_data(self):
        self.info.clear()
        with open('data.txt', 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) !=0:
                for line in lines:
                    data = line.split('|')
                    self.info.append(data)
        return self.info

    def delete_note(self, num: str):
        self.info.clear()
        self.num_d = str(num)
        with open('data.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if self.num_d not in line[0]:
                    self.info.append(line)
        with open('data.txt', 'w', encoding='utf-8') as f:
            n = 1
            for el in self.info:
                num_line = str(n)+el[1:]
                f.write(num_line)
                n+=1