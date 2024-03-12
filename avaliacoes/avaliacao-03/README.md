# RESULTADOS DO CÓDIGO:

![image](https://github.com/mareshbard/PDM2-24-1/assets/125154278/d3a7ed39-f57b-44d1-9937-9e44648753eb)

## Feito em dupla com Antônio Abner

# CÓDIGO:
~~~
import 'dart:io';
import 'dart:async';
import 'dart:isolate';

void main() async {
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

}
~~~
# LAUNCH JSON:

![image](https://github.com/mareshbard/PDM2-24-1/assets/125154278/0e8314e3-e2ab-4ce4-8487-1429c2f60e4f)

