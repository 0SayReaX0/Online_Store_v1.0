
products = [
    {"id": 1, "name": "Хлеб", "price": 30, "stock": 100, "description": "Свежий ржаной хлеб"},
    {"id": 2, "name": "Молоко", "price": 60, "stock": 50, "description": "Молоко 3.2% жирности"},
    {"id": 3, "name": "Яйца", "price": 80, "stock": 150, "description": "Куриные яйца, 10шт"},
    {"id": 4, "name": "Сыр", "price": 200, "stock": 30, "description": "Твердый сыр"},
    {"id": 5, "name": "Колбаса", "price": 250, "stock": 40, "description": "Вареная колбаса"},
    {"id": 6, "name": "Сахар", "price": 50, "stock": 200, "description": "Сахар-песок"},
    {"id": 7, "name": "Масло", "price": 150, "stock": 60, "description": "Сливочное масло"},
    {"id": 8, "name": "Картофель", "price": 40, "stock": 300, "description": "Картофель, 1 кг"},
    {"id": 9, "name": "Морковь", "price": 30, "stock": 200, "description": "Морковь, 1 кг"},
    {"id": 10, "name": "Лук", "price": 20, "stock": 150, "description": "Лук репчатый, 1 кг"},
    {"id": 11, "name": "Гречка", "price": 100, "stock": 100, "description": "Крупа гречневая"},
    {"id": 12, "name": "Рис", "price": 90, "stock": 80, "description": "Рис длиннозерный"},
    {"id": 13, "name": "Мясо", "price": 350, "stock": 20, "description": "Свинина, 1 кг"},
    {"id": 14, "name": "Курица", "price": 200, "stock": 30, "description": "Куриное филе, 1 кг"},
    {"id": 15, "name": "Рыба", "price": 280, "stock": 15, "description": "Свежая рыба, 1 кг"},
    {"id": 16, "name": "Сок", "price": 70, "stock": 50, "description": "Апельсиновый сок"},
    {"id": 17, "name": "Вода", "price": 40, "stock": 100, "description": "Бутилированная вода"},
    {"id": 18, "name": "Чай", "price": 80, "stock": 70, "description": "Черный чай"},
    {"id": 19, "name": "Кофе", "price": 120, "stock": 60, "description": "Растворимый кофе"},
    {"id": 20, "name": "Печенье", "price": 60, "stock": 120, "description": "Печенье с шоколадом"},
]

users = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "user"},
}

user_carts = {}
user_purchase_history = {}


def login():
    while True:
        username = input("Логин: ").strip()
        if not username:
            print("Логин не может быть пустым!")
            continue

        password = input("Пароль: ").strip()
        if not password:
            print("Пароль не может быть пустым!")
            continue

        try:
            if users[username]["password"] == password:
                return username, users[username]["role"]
            else:
                print("Неверный пароль!")

        except KeyError:
            print("Пользователь не найден!")


def show_products(products_list):
    if not products_list:
        print("Продуктов нет!")
        return

    print("-" * 68)
    print("{:<6} {:<15} {:<10} {:<12} {:<20}".format("Номер", "Название", "Цена", "Количество", "Описание"))
    print("-" * 68)

    for product in products_list:
        print("{:<6} {:<15} {:<10} {:<12} {:<20}".format(product["id"], product["name"], product["price"], product["stock"], product["description"]))
    print("-" * 68)


def add_product():
    while True:
        try:
            name = input("Название: ").strip()
            if not name:
                print("Название не может быть пустым!")
                continue

            price = int(input("Цена: "))
            if price <= 0:
                print("Цена должна быть положительным числом!")
                continue

            stock = int(input("Количество: "))
            if stock < 0:
                print("Количество не может быть отрицательным!")
                continue

            description = input("Описание: ").strip()
            if not description:
                print("Описание не может быть пустым!")
                continue

            new_product = {"id": len(products) + 1, "name": name, "price": price, "stock": stock, "description": description}
            products.append(new_product)
            print(f"Продукт '{name}' успешно добавлен.")
            break

        except ValueError:
            print("Неверный формат данных! Проверьте ввод цены и количества.")


def delete_product():
    show_products(products)

    while True:
        try:
            product_id = int(input("Введите номер продукта для удаления: "))
            break
        except ValueError:
            print("Неверный ввод номера! Пожалуйста, введите целое число.")

    product_to_delete = next((p for p in products if p["id"] == product_id), None)
    if product_to_delete is None:
        print("Продукт с таким номером не найден!")
        return

    products.remove(product_to_delete)
    print(f"Продукт '{product_to_delete['name']}' успешно удален!")


def update_product():
    show_products(products)

    while True:
        try:
            product_id = int(input("Введите номер продукта для обновления: "))
            break
        except ValueError:
            print("Неверный ввод номера! Пожалуйста, введите целое число.")

    product_to_update = next((p for p in products if p["id"] == product_id), None)
    if product_to_update is None:
        print("Продукт с таким номером не найден!")
        return

    name_product = product_to_update["name"]
    print("Текущие данные:")
    show_products([product_to_update])

    while True:
        try:
            product_to_update["name"] = input("Новое название (оставьте пустым для сохранения текущего): ").strip() or product_to_update["name"]
            product_to_update["price"] = int(input("Новая цена (оставьте пустым для сохранения текущей): ") or product_to_update["price"])
            product_to_update["stock"] = int(input("Новое количество (оставьте пустым для сохранения текущего): ") or product_to_update["stock"])
            product_to_update["description"] = input("Новое описание (оставьте пустым для сохранения текущего): ").strip() or product_to_update["description"]
            break
        except ValueError:
            print("Неверный формат данных! Проверьте ввод цены и количества.")
    print(f"Продукт '{name_product}' успешно обновлен.")


def filter_products(products_list):
    while True:
        filter_criteria = input("Поиск по названию/цене/количеству/описанию (введите первую букву) или нажмите Enter для пропуска: ").lower().strip()

        if filter_criteria == "н":
            keyword = input(f"Введите ключевое слово для названия: ").lower().strip()
            if not keyword:
                print("Ключевое слово не может быть пустым!")
                continue
            try:
                filter_criteria = "name"
                filtered_products = list(filter(lambda p: keyword in p[filter_criteria].lower(), products_list))
            except KeyError:
                print(f"Некорректный критерий фильтрации: {filter_criteria}")
                continue

        elif filter_criteria == "ц":
            while True:
                try:
                    min_price = int(input("Введите минимальную цену: "))
                    max_price = int(input("Введите максимальную цену: "))
                    if min_price > max_price:
                        print("Минимальная цена не может быть больше максимальной!")
                        continue
                    filtered_products = list(filter(lambda p: min_price <= p["price"] <= max_price, products_list))
                    break
                except ValueError:
                    print("Неверный ввод! Пожалуйста, введите число.")

        elif filter_criteria == "к":
            while True:
                try:
                    min_stock = int(input("Введите минимальное количество: "))
                    max_stock = int(input("Введите максимальное количество: "))
                    if min_stock > max_stock:
                        print("Минимальное количество не может быть больше максимального!")
                        continue
                    filtered_products = list(filter(lambda p: min_stock <= p["stock"] <= max_stock, products_list))
                    break
                except ValueError:
                    print("Неверный ввод! Пожалуйста, введите целое число.")

        elif filter_criteria == "о":
            keyword = input(f"Введите ключевое слово для описания: ").lower().strip()
            if not keyword:
                print("Ключевое слово не может быть пустым!")
                continue
            try:
                filter_criteria = "description"
                filtered_products = list(filter(lambda p: keyword in p[filter_criteria].lower(), products_list))
            except KeyError:
                print(f"Некорректный критерий фильтрации: {filter_criteria}")
                continue

        elif not filter_criteria:
            filtered_products = products_list
            break

        else:
            print("Введите первую букву (например, название - н).")
            continue
        break
    show_products(filtered_products)


def show_users(users_list):
    if not users_list:
        print("Список пользователей пуст.")
        return

    print("-" * 30)
    print("{:<18} {:<10}".format("Имя пользователя", "Роль"))
    print("-" * 30)

    try:
        i = 1
        for username, user_data in users_list.items():
            print(f"{i}. " + "{:<15} {:<10}".format(username, user_data["role"]))
            i += 1
        print("-" * 30)
    except KeyError as e:
        print(f"Некорректные данные пользователя. Отсутствует ключ: {e}")
    except Exception as e:
        print(f"Что-то пошло не так: {e}")


def manage_users():
    print("\n1. Посмотреть всех пользователей")
    print("2. Добавить пользователя")
    print("3. Удалить пользователя")
    print("4. Обновить пароль пользователя")
    print("5. Назад")

    while True:
        try:
            choice = int(input("Выбери цифру (1-5): "))
            if choice not in [1, 2, 3, 4, 5]:
                print("Неверный выбор. Введите число от 1 до 5.")
                continue
            break
        except ValueError:
            print(f"Введите целое число!")

    if choice == 1:
        show_users(users)

    elif choice == 2:
        while True:
            username = input("Логин: ").strip()
            if username in users:
                print("Пользователь с таким логином уже существует!")
                continue
            if not username:
                print("Логин не может быть пустым!")
                continue
            break

        while True:
            password = input("Пароль: ").strip()
            if not password:
                print("Пароль не может быть пустым!")
                continue
            break

        users[username] = {"password": password,"role": "user"}
        print(f"Пользователь '{username}' добавлен.")

    elif choice == 3:
        show_users(users)

        while True:
            username = input("Введите логин для удаления или нажмите Enter для выхода: ").strip()
            if not username:
                break
            if username not in users:
                print("Пользователь не найден.")
                continue
            if username == "admin":
                print("Нельзя удалить этого пользователя!")
                continue
            break

        if username:
            del users[username]
            print(f"Пользователь '{username}' удален.")

    elif choice == 4:
        show_users(users)

        while True:
            username = input("Введите логин для обновления пароля: ").strip()
            if username not in users:
                print("Пользователь не найден.")
                continue
            if not username:
                print("Логин не может быть пустым!")
                continue
            break

        while True:
            password = input("Новый пароль: ").strip()
            if not password:
                print("Пароль не может быть пустым!")
                continue
            break

        users[username]["password"] = password
        print(f"Пароль для пользователя '{username}' обновлен.")

    elif choice == 5:
        pass
    else:
        print("Что-то пошло не так")


def add_to_cart(username):
    show_products(products)

    while True:
        try:
            product_id = int(input("Введите номер продукта для добавления в корзину: "))
            product = next((p for p in products if p["id"] == product_id), None)

            if product is None:
                print("Продукт не найден.")
                continue
            if product["stock"] <= 0:
                print("Этот товар закончился.")
                continue

            while True:
                try:
                    quantity = int(input(f"Введите количество (доступно: {product['stock']}): "))
                    if quantity <= 0:
                        print("Количество должно быть больше нуля!")
                        continue
                    if quantity > product["stock"]:
                        print("Недостаточно товара на складе.")
                        continue
                    break
                except ValueError:
                    print("Неверный ввод! Пожалуйста, введите целое число.")

            if username not in user_carts:
                user_carts[username] = []

            product["stock"] -= quantity
            user_carts[username].append({"product_id": product_id, "quantity": quantity})
            print(f"Продукт '{product["name"]}' добавлен в корзину.")
            break

        except ValueError:
            print("Неверный ввод номера продукта! Пожалуйста, введите целое число.")


def view_cart(username):
    if username not in user_carts or not user_carts[username]:
        print("-" * 25)
        print("Ваша корзина пуста.")
        print("-" * 25)
        return

    print("-" * 25)
    print("Ваша корзина:")
    print("-" * 25)
    total_cost = 0
    cart_items = {}

    try:
        for item in user_carts[username]:
            product_id = item["product_id"]
            quantity = item["quantity"]
            product = next((p for p in products if p["id"] == product_id), None)
            if product is None:
                print(f"Продукт с номером '{product_id}' не найден.")
                continue

            if product_id not in cart_items:
                cart_items[product_id] = {"name": product["name"], "quantity": 0, "price": product["price"]}
            cart_items[product_id]["quantity"] += quantity

        for product_id, item_data in cart_items.items():
            cost = item_data["price"] * item_data["quantity"]
            print(f"- {item_data['name']} x{item_data['quantity']} = {cost} р.")
            total_cost += cost

        print("-" * 25)
        print(f"Сумма: {total_cost} рублей")
        print("-" * 25)

    except (KeyError, TypeError) as e:
        print(f"Проверьте данные в корзине: {e}")


def checkout(username):
    if username not in user_carts or not user_carts[username]:
        print("-" * 25)
        print("Ваша корзина пуста.")
        print("-" * 25)
        return

    view_cart(username)
    while True:
        confirmation = input("Подтвердить покупку (д/н)? ").lower().strip()
        if confirmation in ["д", "н"]:
            break
        print("Неверный ввод. Введите 'д' или 'н'.")

    if confirmation == "д":
        try:
            purchase_items = {}
            total_cost = 0
            for item in user_carts[username]:
                product = next((p for p in products if p["id"] == item["product_id"]), None)
                if product is None:
                    print(f"Товар с номером '{item['product_id']}' не найден.")
                    return

                cost = product["price"] * item["quantity"]
                purchase_items[product["name"]] = purchase_items.get(product["name"], 0) + item["quantity"]
                total_cost += cost

            purchase_items_list = []
            for product_name, quantity in purchase_items.items():
                product = next((p for p in products if p["name"] == product_name), None) #Find product by name
                if product:
                    purchase_items_list.append({"product_name": product_name, "quantity": quantity, "cost": product["price"] * quantity})
                else:
                    print(f"Error: Product '{product_name}' not found in the product list.")
                    return

            user_purchase_history.setdefault(username, []).append(
                {"items": purchase_items_list, "total_cost": total_cost}
            )

            user_carts[username] = []  # Чистка корзины
            print("Заказ успешно оформлен!")

        except (KeyError, TypeError) as e:
            print(f"Ошибка при оформлении заказа: {e}")
    else:
        print("Оформление заказа отменено.")


def view_purchase_history(username):
    if username not in user_purchase_history or not user_purchase_history[username]:
        print("\nИстория покупок отсутствует.")
        return

    purchase_number = 1
    for purchase in user_purchase_history[username]:
        print(f"\nПокупка №{purchase_number}")
        print("-" * 25)
        total_cost = 0

        for item in purchase["items"]:
            print(f"- {item['product_name']} x{item['quantity']} = {item['cost']} р.")
            total_cost += item['cost']

        print("-" * 25)
        print(f"Сумма: {total_cost} рублей")
        print("-" * 25)
        purchase_number += 1


def main():
    i = 0
    stop = True

    while stop:
        if i >= 1:
            exit_program = input("\nДля выхода из программы введите '1': ")
            if exit_program == "1":
                break

        username, role = login()

        while True:
            if role == "admin":
                print(f"\nДобро пожаловать, {username} ({role})!")
                print("1. Добавить товар")
                print("2. Удалить товар")
                print("3. Изменить товар")
                print("4. Посмотреть товары")
                print("5. Управление пользователями")
                print("6. Выход")

                while True:
                    try:
                        choice = int(input("Введите цифру (1-6): "))
                        if 1 <= choice <= 6:
                            break
                        else:
                            print("Выберите цифру от 1 до 6.")
                    except ValueError:
                        print("Неверный ввод. Введите целое число.")

                try:
                    if choice == 1:
                        add_product()
                    elif choice == 2:
                        delete_product()
                    elif choice == 3:
                        update_product()
                    elif choice == 4:
                        filter_products(products)
                    elif choice == 5:
                        manage_users()
                    elif choice == 6:
                        break
                    else:
                        print("Выберите цифру от 1 до 6.")

                except Exception as e:
                        print(f"Произошла ошибка: {e}")

            elif role == "user":
                print(f"\nДобро пожаловать, {username}!")
                print("1. Посмотреть товары")
                print("2. Добавить в корзину")
                print("3. Посмотреть корзину")
                print("4. Оформить заказ")
                print("5. История покупок")
                print("6. Выход")

                while True:
                    try:
                        choice = int(input("Введите цифру (1-6): "))
                        if 1 <= choice <= 6:
                            break
                        else:
                            print("Выберите цифру от 1 до 6.")
                    except ValueError:
                        print("Неверный ввод. Введите целое число.")

                try:
                    if choice == 1:
                        filter_products(products)
                    elif choice == 2:
                        add_to_cart(username)
                    elif choice == 3:
                        view_cart(username)
                    elif choice == 4:
                        checkout(username)
                    elif choice == 5:
                        view_purchase_history(username)
                    elif choice == 6:
                        break
                    else:
                        print("Выберите цифру от 1 до 6.")

                except Exception as e:
                    print(f"Произошла ошибка: {e}")

            else:
                print("Что-то пошло не так!")
                break
        i += 1


if __name__ == "__main__":
    main()