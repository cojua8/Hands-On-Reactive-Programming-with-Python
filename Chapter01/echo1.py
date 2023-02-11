import sys
import rx

# crea un observable a partir de una lista, en este caso la lista de agumentos
argv = rx.from_(sys.argv[1:])

# se subscribe al observable para recibir los eventos
argv.subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed"),
)
