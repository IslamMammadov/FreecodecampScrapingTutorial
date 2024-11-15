# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class FreecodecampPipeline:

    def process_item(self, item, spider):
        adapter =  ItemAdapter(item)
        field_names =  adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                print(value[0].strip())
                adapter[field_name] = value[0].strip()
        
        
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            print(value.lower())
            adapter[lowercase_key] = value.lower()

        price_keys =  ['price','price_exc_tax','price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            print(value)
            adapter[price_key] = float(value)

        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        num_review_string =  adapter.get('num_reviews')
        adapter['num_reviews'] =  int(num_review_string)

        stars_string =  adapter.get('stars')
        split_star_arr = stars_string.split(" ")
        stars_text =  split_star_arr[1].lower()
        if stars_text =='zero':
            adapter['stars'] = 0
        elif stars_text =='one':
            adapter['stars'] = 1
        elif stars_text =='two':
            adapter['stars'] = 2
        elif stars_text =='three':
            adapter['stars'] = 3
        elif stars_text =='four':
            adapter['stars'] = 4
        elif stars_text =='five':
            adapter['stars'] = 5

        return item


import duckdb

class SavetoDuckdbPipeline:

    def __init__(self):
        self.conn = duckdb.connect(r'C:\Users\mislam\Desktop\Backend\DataEng\Scraping2\freecodecamp\freecodecamp\books.db')
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
                         id INTEGER PRIMARY KEY,
                         title nvarchar,
                         product_type nvarchar,
                         price_exc_tax decimal(5,2),
                         price_incl_tax decimal(5,2),
                         tax decimal(5,2),
                         availability integer,
                         num_reviews integer,
                         stars integer,
                         category nvarchar,
                         description text,
                         price decimal(5,2),
                         url nvarchar);"""
                         )
        
    def process_item (self, item, spider):
        insert_query = """ INSERT INTO books (id, title, product_type, price_exc_tax, 
                                              price_incl_tax, tax, availability, 
                                              num_reviews, stars, 
                                              category, description, price, url)
                                              
                            VALUES (nextval('seq_id'),?,?,?,?,?,?,?,?,?,?,?,?)"""
        
        params = (item['title'], item['product_type'], item['price_exc_tax'], 
                item['price_incl_tax'], item['tax'], item['availability'], 
                item['num_reviews'], item['stars'], 
                item['category'], item['description'], item['price'], item['url'])
        
        self.cur.execute(insert_query, params)
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


