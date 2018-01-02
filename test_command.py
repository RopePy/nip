from kuai import Kuai

Kuai.on('go', print)
Kuai.emit('go', 'Hello world')
