CREATE TABLE "customer"(
	"c_id" serial,
	"first_name" varchar (20) NOT NULL,
	"last_name" varchar (20) NOT NULL,
	"c_username" varchar(20),
	"password" varchar(20),
	"balance" numeric(8,2) check ("balance">=0),
	PRIMARY KEY ("c_id")
);

CREATE TABLE "creditcard"(
	"state" varchar(15) NOT NULL,
	"zip" int not null,
	"street" varchar(40) NOT NULL,
	"card_number" int primary key,
	"c_id" serial
);

CREATE TABLE "product"(
	"product_name" varchar(20),
	"product_category" varchar(20),
	"product_id" serial primary key,
	"size" int check("size" > 0)
);

CREATE TABLE "shopping_cart"(
	
	"c_id" serial,
	"product_id" serial,
	"quantity" int check ("quantity">=0)
);

CREATE TABLE "order"(
	"order_id" serial,
	"subtotal" numeric(8,2) NOT NULL,
	"card_number" int,
	"time_ordered" timestamp,
	"status" varchar(10),
	check(status in ('ordered', 'sent', 'received')),
	PRIMARY KEY("order_id")
);
CREATE TABLE "order_details"(
	"quantity" int check("quantity">0) NOT NULL,
	"product_id" serial,
	"order_id" serial,
	PRIMARY KEY("order_id", "product_id")
);

CREATE TABLE "warehouse"(
	"warehouse_id" serial,
	"street" varchar(30) NOT NULL,	
	"zip" int NOT NULL,
	"state" varchar(20) NOT NULL,
	"capacity" int check(capacity>0),
	PRIMARY KEY("warehouse_id")
);

CREATE TABLE "stock"(
	"warehouse_id" serial,
	"quantity" int NOT NULL,
	"product_id" serial,
	PRIMARY KEY("warehouse_id", "product_id")
);

CREATE TABLE "shipping_address"(
	"order_id" serial,
	"state" varchar(20) NOT NULL,
	"street" varchar(40) NOT NULL,
	"zip" int NOT NULL,
	PRIMARY KEY("state", "street", "zip")
);

CREATE TABLE "cost"(
	"product_id" serial,
	"state" varchar(20),
	"price" numeric(8,2) check(price >=0),
	PRIMARY KEY("product_id","state")
);

CREATE TABLE "staff"(
	"first_name" varchar(20) NOT NULL,
	"last_name" varchar(20) NOT NULL,
	"s_id" serial,
	"s_username" varchar(20),
	"password" varchar(20),
	"salary" numeric (8,2) check ("salary" > 0),
	"state" varchar(20) NOT NULL,
	"street" varchar(20) NOT NULL,
	"zip" int NOT NULL,
	PRIMARY KEY("first_name", "last_name")
);
CREATE TABLE "food"(
	"food_category" varchar(20),
	"product_id" serial,
	"calories" int check(calories > 0),
	PRIMARY KEY("product_id")
);

CREATE TABLE "alcohol"(
	"alcohol_category" varchar(20),
	"alcohol_content" numeric (3,1),
	"product_id" serial,
	PRIMARY KEY("product_id")
);

ALTER TABLE "creditcard" ADD FOREIGN KEY ("c_id") REFERENCES "customer"("c_id"); 
ALTER TABLE "shopping_cart" ADD FOREIGN KEY ("c_id") REFERENCES "customer"("c_id");
ALTER TABLE "order" ADD FOREIGN KEY ("card_number") REFERENCES "creditcard"("card_number");
ALTER TABLE "order_details" ADD FOREIGN KEY ("product_id") REFERENCES "product"("product_id");
ALTER TABLE "order_details" ADD FOREIGN KEY ("order_id") REFERENCES "order"("order_id");
ALTER TABLE "stock" ADD FOREIGN KEY ("warehouse_id") REFERENCES "warehouse"("warehouse_id");
ALTER TABLE "cost" ADD FOREIGN KEY ("product_id") REFERENCES "product"("product_id");
ALTER TABLE "food" ADD FOREIGN KEY ("product_id") REFERENCES "product"("product_id");
ALTER TABLE "alcohol" ADD FOREIGN KEY ("product_id") REFERENCES "product"("product_id");