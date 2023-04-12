from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import registry

import model

metadata = MetaData()

order_lines = Table("order_lines", metadata, Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("sku", String(255)), Column("qty", Integer, nullable=False), Column("orderid", String(255)))


def start_mappers():
    # lines_mapper = registry.map_imperatively(model.OrderLine, order_lines)
    lines_mapper = registry.map_imperatively()
