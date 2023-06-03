from django.db import connections


def custom_sql(conn, query):
    with connections[conn].cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def custom_procedure(conn, procedure, procedure_args=None):
    with connections[conn].cursor() as cursor:
        if procedure_args:
            cursor.callproc(procedure, procedure_args)
        else:
            cursor.callproc(procedure)

        columns = [col[0] for col in cursor.description]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def movecol(df, cols_to_move=[], ref_col='', place='After'):
    cols = df.columns.tolist()
    if place == 'After':
        seg1 = cols[:list(cols).index(ref_col) + 1]
        seg2 = cols_to_move
    if place == 'Before':
        seg1 = cols[:list(cols).index(ref_col)]
        seg2 = cols_to_move + [ref_col]

    seg1 = [i for i in seg1 if i not in seg2]
    seg3 = [i for i in cols if i not in seg1 + seg2]

    return (df[seg1 + seg2 + seg3])


def custom_procedure_multiple_results(conn, procedure, procedure_args=None):
    with connections[conn].cursor() as cursor:
        if procedure_args:
            cursor.callproc(procedure, procedure_args)
        else:
            cursor.callproc(procedure)

        first_resultset = cursor.fetchone()

        cursor.nextset()

        columns = [col[0] for col in cursor.description]
        second_resultset = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        return [first_resultset, second_resultset]