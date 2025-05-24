import psycopg2
from psycopg2 import Error


# Hàm chèn dữ liệu vào cơ sở dữ liệu PostgreSQL
def insert_data_to_database(dataList):
    connection = None
    cursor = None
    try:
        # Kết nối đến cơ sở dữ liệu PostgreSQL
        connection = psycopg2.connect(
            host='postgres',
            database='airflow',
            user='airflow',
            password='airflow'
        )
        cursor = connection.cursor()

        # Tạo bảng nếu chưa tồn tại
        create_table_query = """
        CREATE TABLE IF NOT EXISTS articles (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            time TIMESTAMP,
            author TEXT,
            summary TEXT
        );
        """
        cursor.execute(create_table_query)

        # Kiểm tra xem bảng có dữ liệu không
        cursor.execute("SELECT COUNT(*) FROM articles")
        count = cursor.fetchone()[0]

        # Nếu bảng có dữ liệu, xóa toàn bộ và reset ID
        if count > 0:
            cursor.execute("TRUNCATE TABLE articles RESTART IDENTITY CASCADE")
            connection.commit()
            print("Đã xóa toàn bộ dữ liệu cũ và reset ID")

        
        for data in dataList:
            # Câu lệnh SQL để chèn dữ liệu
            sql_insert_query = """ 
            INSERT INTO articles (title, url, time, author, summary)
            VALUES (%s, %s, %s, %s, %s) 
            """
            values = (data['Title'], data['Link'], data['Date'], data['Author'], data['Summary'])
            cursor.execute(sql_insert_query, values)

            # Lưu thay đổi
            connection.commit()
            print(f"Dữ liệu của '{data['Title']}' đã được chèn thành công vào cơ sở dữ liệu.")

        return True
    except Error as e:
        print(f"Lỗi khi chèn dữ liệu vào cơ sở dữ liệu: {e}")
        return False
    finally:
        # Đảm bảo đóng kết nối và con trỏ
        if cursor:
            cursor.close()
        if connection:
            connection.close()

