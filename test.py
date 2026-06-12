
import logging


logging.basicConfig(
    filename="product_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

product_db = [
    {
        "product_id": "P01",
        "product_name": "Coca Cola",
        "price": 15000,
        "quantity": 15
    },
    {
        "product_id": "P02",
        "product_name": "Pepsi",
        "price":12000,
        "quantity": 20
    },
    {
        "product_id": "P03",
        "product_name": "Sprite",
        "price": 20000,
        "quantity": 18
    }
]

def display_products(product):
    if len(product_db) == 0:
        print("chưa có sản phẩm nào")
    else:
        print("STT | ID  | TÊN SẢN PHẨM | GIÁ | SỐ LƯỢNG")

        for index, product in enumerate(product_db, start=1):
            print(
                f"{index} | "
                f"{product['product_id']} | "
                f"{product['product_name']} | "
                f"{product['price']} | "
                f"{product['quantity']}"
            )

        logging.info("User viewed product list.")

def add_product(product):
    product_id = input("Nhập mã sản phẩm: ").upper()

    for product in product_db:
        if product["product_id"] == product_id:
            print("Mã sản phẩm đã tồn tại.")
            logging.warning(f"Duplicate product ID {product_id}")
            return

    product_name = input("Nhập tên sản phẩm: ")

    while True:
        try:
            price = int(input("Nhập giá sản phẩm: "))

            if price <= 0:
                print("Giá phải lớn hơn 0.")
                continue

            break

        except ValueError:
            print("Giá phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input")

    while True:
        try:
            quantity = int(input("Nhập số lượng sản phẩm: "))

            if quantity <= 0:
                print("Số lượng phải lớn hơn 0.")
                continue

            break

        except ValueError:
            print("Số lượng phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid quantity input")

    new_product = {
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }

    product_db.append(new_product)

    print("Thêm sản phẩm thành công.")
    logging.info(f"Added new product {product_id}")


def update_product(products):
    product_id = input("Nhập mã sản phẩm cần sửa: ").upper()

    for product in products:
        if product["product_id"].upper() == product_id:

            product["product_name"] = input("Nhập tên mới: ")

            while True:
                try:
                    new_price = int(input("Nhập giá mới: "))

                    if new_price <= 0:
                        print("Giá phải lớn hơn 0.")
                        continue

                    product["price"] = new_price
                    break

                except ValueError:
                    print("Giá phải là số.")

            while True:
                try:
                    new_quantity = int(input("Nhập số lượng mới: "))

                    if new_quantity <= 0:
                        print("Số lượng phải lớn hơn 0.")
                        continue

                    product["quantity"] = new_quantity
                    break

                except ValueError:
                    print("Số lượng phải là số.")

            print("Cập nhật thành công.")
            logging.info(f"Updated product {product_id}")
            return

    print("Không tìm thấy sản phẩm.")
    logging.warning(f"Product {product_id} not found")

if __name__ == "__main__":

    while True:
        print("""
        ===== HỆ THỐNG QUẢN LÝ SẢN PHẨM =====

        1. Hiển thị danh sách sản phẩm
        2. Thêm sản phẩm
        3. Cập nhật sản phẩm
        4. Thoát

        ==============================
        """)
        choice = input("Mời bạn nhập lựa chọn 1-4: ")
        if choice == "1":
            display_products(product_db)
        if choice == "2":
            add_product(product_db)
        if choice == "3":
            update_product(product_db)
        if choice == "4":
            print("Đã thoát chương trình!")
            break
