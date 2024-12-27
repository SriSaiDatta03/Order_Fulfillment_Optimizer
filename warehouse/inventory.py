import psycopg2

class InventoryManager:
    def __init__(self,db_config):
        self.conn=psycopg2.connect(**db_config)

    def get_low_stock_items(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT product_name FROM inventory WHERE stock_quantity <= reorder_level")
            return cur.fetchall()