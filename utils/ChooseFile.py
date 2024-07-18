from src.FileManager import FileManager


class ChooseFile:
    def show_menu(self):
        print("Seleccione el contenido que desea guardar:")
        print("1. Contenido original")
        print("2. Contenido enriquecido")
        print("3. Contenido traducido")
        print("4. Salir")

    def show_format_menu(self):
        print("Seleccione el formato en que desea guardar el contenido:")
        print("1. PDF")
        print("2. TXT")
        print("3. Volver al menú principal")

    def main(self, content):
        while True:
            try:
                self.show_menu()
                choice = input("Ingrese su elección (1-4): ")

                if choice in ['1', '2', '3']:
                    if choice == '1':
                        selected_content = content.original_content
                        default_filename = "original"
                    elif choice == '2':
                        selected_content = content.enriched_content
                        default_filename = "enriched"
                    elif choice == '3':
                        selected_content = content.translated_content
                        default_filename = "translated"

                    file_manager = FileManager(selected_content, default_filename)

                    while True:
                        try:
                            self.show_format_menu()
                            format_choice = input("Ingrese su elección de formato (1-3): ")

                            if format_choice == '1':
                                file_manager.save_as_pdf()
                                break
                            elif format_choice == '2':
                                file_manager.save_as_txt()
                                break
                            elif format_choice == '3':
                                break
                            else:
                                print("Opción no válida. Intente de nuevo.")
                        except Exception as e:
                            print(f"Error processing format choice: {e}")
                elif choice == '4':
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            except Exception as e:
                print(f"Error processing main menu choice: {e}")


