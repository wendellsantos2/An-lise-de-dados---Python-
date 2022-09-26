import mysql.connector
class DbUtil():
    def connection():
        conn = mysql.connector.connect(
            host="localhost", 
            port=3306,
            user="root",
            password="", 
            db="enderecos"
        )
        return conn

    
    @staticmethod
    def enviar_para_banco(itens):
        conn = DbUtil.connection()   
        cursor = conn.cursor()
        sql = f"""insert ignore into ceps(cep,estado,rua,bairro,complemento) values """  
        cursor.execute(sql + itens)
        conn.commit()
        print("Dados enviados para o Banco de dados com sucesso !") 
 
    def consultar_endereco(buscar_enderecos):
        conn = DbUtil.connection()
        cursor = conn.cursor()
        sql = f"""SELECT cep,estado,rua,bairro,complemento FROM ceps where cep = '{buscar_enderecos}'"""
        cursor.execute(sql)
        result = cursor.fetchone()
        print(f"Cep : {result[0]}, Estado : {result[1]},Rua: {result[2]}, bairro: {result[3]}, complemento {result[4]} ")
        return result   
        