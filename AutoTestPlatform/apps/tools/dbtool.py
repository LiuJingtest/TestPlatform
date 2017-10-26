# 数据库处理工具
import pymysql
import contextlib


@contextlib.contextmanager
def connDB(host, user, pwd, db_name, charset="utf-8"):
    db_conn = pymysql.connect(host=host, user=user, password=pwd, db=db_name, charset=charset)
    db_cursor = db_conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield db_cursor
    except Exception as e:
        print(e)
        db_conn.rollback()
        db_cursor.close()
        db_conn.close()
    finally:
        db_conn.commit()
        db_cursor.close()
        db_conn.close()


if __name__ == '__main__':
    test = { "host":"192.168.32.121",  "user":"root",  "pwd":"EV6ZeYVa",  "db_name":"testoa3",  "charset":"utf8mb4" }
    with connDB(**test) as db_cursor:
        db_cursor.execute("""INSERT INTO `testoa3`.`oa_org` (`company_id`, `org_name`, `parent_org_id`,
                          `org_points`, `org_all_points`, `all_children_id`, `all_parent_id`) VALUES ('1',
                          '测试部门', '2', '0', '0', '89', '2,89');
                          DELETE FROM `oa_org` WHERE (`org_name`='测试部门')""")