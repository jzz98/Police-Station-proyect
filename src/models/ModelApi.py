class Apis:
    @classmethod
    def recluseApi(cls, db):
        try:
            cursor = db.connection.cursor()
            sql1 = "SELECT * FROM Reclusos"
            cursor.execute(sql1)
            rows = cursor.fetchall()  # Trae todos los datos
            
            
            if rows:
                # Opcional: convertir las filas en diccionarios
                columns = [desc[0] for desc in cursor.description]
                result = []
                for row in rows:
                    result.append(dict(zip(columns, row)))

                return result
            else:
                return None

        except Exception as exp:
            raise Exception(f"Error in recluseApi: {exp}")

