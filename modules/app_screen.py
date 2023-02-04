import customtkinter
# створюємо клас App 
class App(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        print(self.PC_SCREEN_HEIGHT)
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")


        # встановлюємо розмір додатку та його розташування на екрані комп'ютера

        add_x = 0
        add_y = 0

        # зліва зверху
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{add_x}+{add_y}")

        # справа зверху
        # add_x = self.PC_SCREEN_WIDTH - self.APP_WIDTH
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{add_x}+{0}")

        # посередині
        # add_x = self.PC_SCREEN_WIDTH // 2 - self.APP_WIDTH // 2
        # add_y = self.PC_SCREEN_HEIGHT // 2 - self.APP_HEIGHT // 2
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{add_x}+{add_y}")

        # зліва снизу
        # add_y = self.PC_SCREEN_HEIGHT - self.APP_HEIGHT
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{add_y}")

        # справа снизу
        # add_x = self.PC_SCREEN_WIDTH - self.APP_WIDTH
        # add_y = self.PC_SCREEN_HEIGHT - self.APP_HEIGHT
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{add_x}+{add_y}")


# створюємо об'єкт від класу App
app = App(app_width=400, app_height=300)