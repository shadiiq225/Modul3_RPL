from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
            val = (nama, alamat)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    def update_anggota(self, id_anggota, nama, alamat):
        """Fungsi untuk memperbarui data anggota berdasarkan id_anggota"""
        try:
            cursor = self.conn.cursor()
            query = "UPDATE anggota SET nama = %s, alamat = %s WHERE id_anggota = %s"
            cursor.execute(query, (nama, alamat, id_anggota))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saat memperbarui data: {e}")
            return False

    def delete_anggota(self, id_anggota):
        """Fungsi untuk menghapus data anggota berdasarkan id_anggota"""
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM anggota WHERE id_anggota = %s"
            cursor.execute(query, (id_anggota,))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saat menghapus data: {e}")
            return False