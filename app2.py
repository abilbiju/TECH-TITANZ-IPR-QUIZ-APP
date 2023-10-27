from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class IntellectualPropertyQuizApp(App):
    def build(self):
        self.score = 0
        self.all_questions = [
            {"question": "What does 'IP' stand for in 'IP rights'?",
             "options": ["Intellectual Property", "Internet Protocol", "Innovative Product"],
             "answer": "Intellectual Property"},

            {"question": "Which type of intellectual property protects inventions?",
             "options": ["Patent", "Trademark", "Copyright"],
             "answer": "Patent"},

            {"question": "What is the term for exclusive rights granted to authors of original works?",
             "options": ["Patent", "Copyright", "Trademark"],
             "answer": "Copyright"},

            {"question": "Which symbol is used to indicate a registered trademark?",
             "options": ["™", "®", "©"],
             "answer": "®"},
            {"question": "Which type of intellectual property protects the way a product looks?",
 "options": ["Patent", "Trademark", "Design Right"],
 "answer": "Design Right"},

{"question": "What is the term for a word, phrase, symbol, or design that identifies and distinguishes a source of goods or services?",
 "options": ["Patent", "Trademark", "Copyright"],
 "answer": "Trademark"},

{"question": "Which type of intellectual property protects original works of authorship?",
 "options": ["Patent", "Trademark", "Copyright"],
 "answer": "Copyright"},

{"question": "Which type of intellectual property protects new and useful processes, machines, and compositions of matter?",
 "options": ["Patent", "Trademark", "Copyright"],
 "answer": "Patent"},

{"question": "Which intellectual property right allows the creator of an original work to have control over how it is used and distributed?",
 "options": ["Patent", "Trademark", "Copyright"],
 "answer": "Copyright"},

{"question": "What does the 'TM' symbol indicate?",
 "options": ["Trademark", "Patent", "Copyright"],
 "answer": "Trademark"},

{"question": "What is a trade secret?",
 "options": ["A type of patent", "A confidential business information", "A trademark symbol"],
 "answer": "A confidential business information"},

{"question": "Which intellectual property right protects the way an invention looks, its decorative aspects, and design?",
 "options": ["Trademark", "Copyright", "Design Patent"],
 "answer": "Design Patent"},

{"question": "What does 'Fair Use' mean in copyright law?",
 "options": ["Using copyrighted material without permission", "Using copyrighted material for educational or criticism purposes", "Copying copyrighted material for commercial use"],
 "answer": "Using copyrighted material for educational or criticism purposes"},

{"question": "What is a utility patent?",
 "options": ["A patent for a useful machine or process", "A patent for decorative designs", "A patent for a novel and useful book"],
 "answer": "A patent for a useful machine or process"},

{"question": "What is the duration of copyright protection for most works in the United States?",
 "options": ["Lifetime of the creator plus 70 years", "Lifetime of the creator plus 50 years", "10 years from the date of creation"],
 "answer": "Lifetime of the creator plus 70 years"},

{"question": "What is the primary purpose of intellectual property rights?",
 "options": ["To protect the interests of large corporations", "To encourage innovation and creativity", "To restrict access to information"],
 "answer": "To encourage innovation and creativity"},

{"question": "Which type of intellectual property protection is typically the easiest and least expensive to obtain?",
 "options": ["Trademark", "Copyright", "Patent"],
 "answer": "Copyright"},

{"question": "What does 'Public Domain' mean in copyright law?",
 "options": ["Works that are freely available to the public", "Works that are restricted and cannot be used", "Works created by the government"],
 "answer": "Works that are freely available to the public"},

{"question": "What is a 'Cease and Desist' letter?",
 "options": ["A letter from a friend", "A letter from the government", "A legal notice to stop an unauthorized activity"],
 "answer": "A legal notice to stop an unauthorized activity"},

{"question": "What is the primary function of a trademark?",
 "options": ["To protect the appearance of a product", "To identify the source of goods or services", "To prevent others from using similar words"],
 "answer": "To identify the source of goods or services"},

{"question": "What does 'Infringement' mean in intellectual property law?",
 "options": ["Protecting intellectual property rights", "Copying or using someone else's intellectual property without permission", "Creating new intellectual property"],
 "answer": "Copying or using someone else's intellectual property without permission"},

{"question": "What is the term for a legal right granted to inventors to exclude others from making, using, and selling their inventions?",
 "options": ["Trademark", "Patent", "Copyright"],
 "answer": "Patent"}

        ]
        self.current_question = 0
        self.questions_per_round = 5  # Number of questions to ask per round
        self.questions = random.sample(self.all_questions, self.questions_per_round)

        # Outer layout to hold questions and buttons
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        # Title label with default font
        title_label = Label(text="Tech Titanz Quiz App", font_size=36)
        self.layout.add_widget(title_label)

        # Layout for questions and answer buttons
        self.question_layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.question_layout)

        # Layout for "Try Again" and "Reset" buttons
        self.button_layout = BoxLayout(orientation="horizontal")
        self.layout.add_widget(self.button_layout)

        self.question_label = Label(text=self.questions[self.current_question]["question"], font_size=24)
        self.question_layout.add_widget(self.question_label)

        self.answer_buttons = []
        for option in self.questions[self.current_question]["options"]:
            button = Button(text=option, font_size=18, background_color=(0.2, 0.6, 0.2, 1))
            button.bind(on_press=self.select_answer)
            self.answer_buttons.append(button)
            self.question_layout.add_widget(button)

        self.reset_button = Button(text="Reset", on_press=self.reset_quiz, size_hint=(None, None), size=(100, 50), background_color=(0.9, 0.2, 0.2, 1))
        self.try_again_button = Button(text="Try Again", on_press=self.try_again, size_hint=(None, None), size=(100, 50), background_color=(0.2, 0.9, 0.2, 1), disabled=True)
        self.button_layout.add_widget(self.reset_button)
        self.button_layout.add_widget(self.try_again_button)

        return self.layout

    # Rest of the code remains the same

    
    def select_answer(self, instance):
        selected_answer = instance.text
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < self.questions_per_round:
            self.question_label.text = self.questions[self.current_question]["question"]
            # Update answer buttons for the new question
            for i, option in enumerate(self.questions[self.current_question]["options"]):
                self.answer_buttons[i].text = option
            # Reset button backgrounds
            for button in self.answer_buttons:
                button.background_color = (1, 1, 1, 1)
        else:
            self.show_score()

    def show_score(self):
        score_message = f"Quiz Complete!\nYour Score: {self.score}/{self.questions_per_round}"
        popup = Popup(title="Quiz Result", content=Label(text=score_message), size_hint=(None, None), size=(400, 200))
        popup.open()

        # Disable answer buttons after the quiz is complete
        for button in self.answer_buttons:
            button.disabled = True

        # Enable the "Try Again" button
        self.try_again_button.disabled = False

    def reset_quiz(self, instance):
        self.score = 0
        self.current_question = 0
        self.questions = random.sample(self.all_questions, self.questions_per_round)
        self.try_again_button.disabled = True
        self.show_next_question()

    def try_again(self, instance):
        self.score = 0
        self.current_question = 0
        self.questions = random.sample(self.all_questions, self.questions_per_round)
        self.try_again_button.disabled = True
        self.show_next_question()

    def show_next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.text = question_data["question"]

            # Randomly shuffle the answer options
            answer_options = random.sample(question_data["options"], len(question_data["options"]))

            for i, button in enumerate(self.answer_buttons):
                button.text = answer_options[i]
                button.background_color = (1, 1, 1, 1)  # Reset button colors
                button.disabled = False
        else:
            self.show_score()

if __name__ == '__main__':
    IntellectualPropertyQuizApp().run()
