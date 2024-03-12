# RESULTADOS DO CÓDIGO:

![image](https://github.com/mareshbard/PDM2-24-1/assets/125154278/899d5022-b073-4ac1-a3a5-f67c0d1be288)
## Feito em dupla com Antônio Abner

# CÓDIGO:
~~~
import 'dart:io';
import 'dart:async';
import 'dart:isolate';

void main() async {
    print('Antonio Abner Soares Jeronimo');
    print('Leticia Vitória Pereira Gomes');
    

  final receivePort = ReceivePort();
  await Isolate.spawn(doAsyncOperation, receivePort.sendPort);

  print('Iniciando outras tarefas...');
  await Future.delayed(Duration(seconds: 1));
  print('Continuando outras tarefas...');

  final result = await receivePort.first;
  print('Resultado: $result');
}

void doAsyncOperation(SendPort sendPort) async {
  final result = await File('./16-programacao-assincrona/arquivo.txt').readAsString();
  sendPort.send(result);
}
~~~
# LAUNCH JSON:

![image](https://github.com/mareshbard/PDM2-24-1/assets/125154278/0e8314e3-e2ab-4ce4-8487-1429c2f60e4f)

