import rx
import rx.operators as ops
from rx.subject.subject import Subject
from rx.core.observer.observer import Observer


# recibe un observable y devuelve otro observable
def component_a(observable):
    return observable.pipe(ops.map(lambda i: i * 2))


# recibe un observable y devuelve otro observable
def component_b(observable):
    observer = Observer(
        on_next=lambda i: print("item: {}".format(i)),
        on_error=lambda e: print("error: {}".format(e)),
        on_completed=lambda: print("completed"),
    )

    observable.subscribe(observer)
    return rx.from_([1, 2, 3])  # este es el punto de partida


proxy = Subject()  # el proxy actua como observador y como observable
b_out = component_b(proxy)  # aqui proxy es el observable
a_out = component_a(b_out)  # aqui se conectan los dos componentes
a_out.subscribe(proxy)  # aqui proxy es el observador

# no importa quien se conecte primero, el programa funciona al ejecutar la
# subscripcion
a_in_proxy = Subject()
a_out = component_a(a_in_proxy)
b_out = component_b(a_out)
b_out.subscribe(a_in_proxy)
