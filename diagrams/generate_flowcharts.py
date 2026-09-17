import subprocess

todo = {"biseccion":["biseccion", "ejecutar_biseccion", "evaluar_polimonio"]}

for file in todo:
    for func in todo[file]:
        subprocess.run(["pyflowchart", f"../src/modules/{file}.py", "-o", f"{func}.html", "-f", func])