from Save_as_pdf import save_as_pdf, save_as_txt, show_menu, show_format_menu
from Save_as_pdf import original_content, enriched_content, translated_content

def main():
    while True:
        try:
            show_menu()
            choice = input("Ingrese su elección (1-4): ")

            if choice in ['1', '2', '3']:
                if choice == '1':
                    content = original_content
                    default_filename = "original"
                elif choice == '2':
                    content = enriched_content
                    default_filename = "enriched"
                elif choice == '3':
                    content = translated_content
                    default_filename = "translated"

                while True:
                    try:
                        show_format_menu()
                        format_choice = input("Ingrese su elección de formato (1-3): ")

                        if format_choice == '1':
                            save_as_pdf(content, default_filename + ".pdf")
                            break
                        elif format_choice == '2':
                            save_as_txt(content, default_filename + ".txt")
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

if __name__ == "__main__":
    main()
