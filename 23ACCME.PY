from time import sleep


class Stereotypes:
    def __init__(self):
        self.American = 0
        self.British = 0
        self.Irish = 0
        self.German = 0
        self.Scandanavian = 0
        self.Indian = 0
        self.African = 0
        self.Chinese = 0
        self.Japanese = 0
        self.Arab = 0
        self.Italian = 0
        self.French = 0
        self.Russian = 0
        self.questionBase = "On a scale of 1 - 10, 10 being max, "
        pass

    def askQuestion(self, question):
        scale = int(input(self.questionBase + question + " "))
        return scale

    def Compile(self):
        total = (
            self.American
            + self.African
            + self.Arab
            + self.British
            + self.Chinese
            + self.French
            + self.German
            + self.Indian
            + self.Irish
            + self.Italian
            + self.Japanese
            + self.Russian
            + self.Scandanavian
        )
        print(
            f"""According to the test I would say you are: 
                {'%.2f'%(100 * self.American / total)}% American
                {'%.2f'%(100 * self.Irish / total)}% Irish
                {'%.2f'%(100 * self.German / total)}% German
                {'%.2f'%(100 * self.British / total)}% British
                {'%.2f'%(100 * self.Scandanavian / total)}% Scandanavian
                {'%.2f'%(100 * self.Indian / total)}% Indian
                {'%.2f'%(100 * self.African / total)}% African
                {'%.2f'%(100 * self.Chinese / total)}% Chinese
                {'%.2f'%(100 * self.Japanese / total)}% Japanese
                {'%.2f'%(100 * self.Arab / total)}% Arab
                {'%.2f'%(100 * self.Italian / total)}% Italian
                {'%.2f'%(100 * self.French / total)}% French
                {'%.2f'%(100 * self.Russian / total)}% Russian                
                """
        )

    def Start(self):
        q1 = "What is your name? "
        q2 = "How old are you? "
        q3 = "What country are you living in? "
        q4 = "Do you understand that this is a joke and anything you enter won't be saved so go crazy! "
        qs = [q1, q2, q3, q4]
        for q in qs:
            a = input(q)

    def America(self):
        q1 = "how much do you love guns?"
        q2 = "how important is capitalism?"
        q3 = "how not racist is America?"
        q4 = "do you enjoy large portions of food?"
        q5 = "how free to do whatever you want are you?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.American += self.askQuestion(q)

    def Britain(self):
        q1 = "how messed up are your teeth?"
        q2 = "how much tea do you consume?"
        q3 = "how much do you talk about the weather?"
        q4 = "do you think a monarch is important?"
        q5 = "are queues important in everyday life?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.British += self.askQuestion(q)

    def Ireland(self):
        q1 = "do you have a short temper?"
        q2 = "how much do you enjoy the colour green?"
        q3 = "is your hair red?"
        q4 = "do you enjoy potatoes?"
        q5 = "how short are you?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Irish += self.askQuestion(q)

    def Germany(self):
        q1 = "how much do you enjoy beer?"
        q2 = "how much do you enjoy sausages?"
        q3 = "how punctual to events are you?"
        q4 = "do you not have a sense of humour?"
        q5 = "how fast are you at getting tasks done?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.German += self.askQuestion(q)

    def Scandanavia(self):
        q1 = "how much do you like vikings?"
        q2 = "how much do you eat meatballs?"
        q3 = "how much do you eat Danish pastries?"
        q4 = "do you enjoy the cold?"
        q5 = "how much of a rude person are you?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Scandanavian += self.askQuestion(q)

    def India(self):
        q1 = "how much do you enjoy spicy food?"
        q2 = "do you worship animals?"
        q3 = "do you enjoy scamming people?"
        q4 = "are you poor?"
        q5 = "are you good with computers?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Indian += self.askQuestion(q)

    def Africa(self):
        q1 = "how much do you enjoy water?"
        q2 = "how much do you prefer primitive technology?"
        q3 = "do you believe that people of higher power are corrupted?"
        q4 = "do you like large piercings?"
        q5 = "do you understand the differences between a continent and a country?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.African += self.askQuestion(q)

    def China(self):
        q1 = "would you eat your pet in an emergency?"
        q2 = "do you enjoy martial arts?"
        q3 = "how good are you at maths?"
        q4 = "do you think you have been brainwashed?"
        q5 = "how well do you understand english?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Chinese += self.askQuestion(q)

    def Japan(self):
        q1 = "how much do you love swords and thick armour?"
        q2 = "how important is hiding in the backround to you?"
        q3 = "are you a polite person?"
        q4 = "do you enjoy watching cartoons with big eyes?"
        q5 = "how much do you know about modern technology?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Japanese += self.askQuestion(q)

    def Arabic(self):
        q1 = "how much do explosions affect you?"
        q2 = "how rich are you?"
        q3 = "how much do you enjoy the desert?"
        q4 = "do you think you are oppressed by the people in your life?"
        q5 = "do you think everyone looks the same?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Arab += self.askQuestion(q)

    def Italy(self):
        q1 = "how much do you love pizza?"
        q2 = "how much do you love pasta?"
        q3 = "how much power do you think the mafia has?"
        q4 = "do you like to talk with your hands?"
        q5 = "how important is food in your life?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Italian += self.askQuestion(q)

    def France(self):
        q1 = "what are the chances you'd lose a fight?"
        q2 = "is eating bread important to you?"
        q3 = "would you eat slimy creatures?"
        q4 = "would you describe yourself as lazy?"
        q5 = "is smoking important to you?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.French += self.askQuestion(q)

    def Russia(self):
        q1 = "is vodka like water to you?"
        q2 = "is communism a good thing?"
        q3 = "would you do something crazy becuase why not?"
        q4 = "from all guns would an ak47 be in your top 10?"
        q5 = "in a fight with a bear do you think you'd win?"
        qs = [q1, q2, q3, q4, q5]
        for q in qs:
            self.Russian += self.askQuestion(q)

    def main(self):
        print(
            "Hi, and welcome to 23 According to Me.\nThis is where I think your DNA is from based on answers from all 69 question I'll ask, please enjoy and have fun!"
        )
        self.Start()
        self.America()
        self.Britain()
        self.Ireland()
        self.Germany()
        self.Scandanavia()
        self.India()
        self.Africa()
        self.China()
        self.Japan()
        self.Arabic()
        self.Italy()
        self.France()
        self.Russia()
        print("Compiling Results")
        sleep(10)
        self.Compile()


TWENTYTHREE = Stereotypes()
TWENTYTHREE.main()
