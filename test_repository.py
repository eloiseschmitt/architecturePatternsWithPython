import model
import repository


def test_repository_can_save_a_batch(session):
    batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(batch)
    session.commit()

    rows = list(session.execute("SELECT reference, sku, _purchased_quantity, eta FROM 'batches'"))
    assert rows == [("batch1", "RUSTY-SOAPDISH", 100, None)]


def insert_order_lines(session):
    session.execute("INSERT INTO order_lines (orderid, sku, qty) VALUES ('order1', 'GENERIC-SOFA', 12)")
    [[orderline_id]] == session.execute("SELECT id FROM order_line WHERE orderid=:orderid AND sku=:sku",
                                        dict(orderid='order1', sku="GENERIC-SOFA"))
    return orderline_id