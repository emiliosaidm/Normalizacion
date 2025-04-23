# ITAM Primavera 2025 - Tarea de Normalización

Presentamos a continuación algunos resultados obtenidos al poner a prueba los métodos implementados, utilizando tanto dependencias funcionales como multivaluadas.

## Pruebas

```python
from normalization.components import Relvar, FunctionalDependency, MultivaluedDependency, Attribute
from normalization.algorithms import closure, is_superkey, is_key, is_relvar_in_4nf, is_relvar_in_bcnf
import numpy as np
import matplotlib.pyplot as plt
```

```python
df1 = FunctionalDependency("{CLABE} -> {Nombre, Apellido, RFC}")
df1.is_trivial()
```

    False

```python
dmv1 = MultivaluedDependency("{RFC} ->-> {CLABE}")
dmv1.is_trivial(heading={Attribute("CLABE"), Attribute("RFC")})
```

    True

```python
df1 = FunctionalDependency("{A} -> {B}")
df2 = FunctionalDependency("{B} -> {C}")
df3 = FunctionalDependency("{A,D} -> {E}")

closure(
    attributes={Attribute("A")},
    functional_dependencies={df1,df2,df3}
)
```

    {Attribute(name='A'), Attribute(name='B'), Attribute(name='C')}

```python
df1 = FunctionalDependency("{A} -> {B, E}")
df2 = FunctionalDependency("{B} -> {C}")
df3 = FunctionalDependency("{A,D} -> {E}")
df4 = FunctionalDependency("{E} -> {A,B,C}")

is_superkey(
    attributes={Attribute("A"), Attribute("E")},
    functional_dependencies={df1,df2,df3},
    heading={Attribute(name='A'), Attribute(name='B'), Attribute(name='C'),  Attribute(name='E')}
)
```

    True

```python
df1 = FunctionalDependency("{A} -> {B,D}")
df2 = FunctionalDependency("{B} -> {C}")

is_key(
    attributes={Attribute("A")},
    functional_dependencies={df1,df2},
    heading={Attribute(name='A'), Attribute(name='B'), Attribute(name='C'), Attribute(name='D')}
)
```

    True

```python
fd1 = FunctionalDependency("{A} -> {B}")
fd2 = FunctionalDependency("{B} -> {C}")
fd3 = FunctionalDependency("{C} -> {A}")
relvar = Relvar(
    {"A", "B", "C"},
    {fd1, fd2, fd3}
)

is_relvar_in_bcnf(relvar)

```

    True

```python
fd = FunctionalDependency("{EstudianteID} -> {Curso, Club}")

mfd1 = MultivaluedDependency("{EstudianteID} ->-> {Curso}")
mfd2 = MultivaluedDependency("{EstudianteID} ->-> {Club}")

relvar_4nf = Relvar(
    heading={"EstudianteID", "Curso", "Club"},
    functional_dependencies={fd},
    multivalued_dependencies={mfd1, mfd2}
)

print(is_relvar_in_4nf(relvar_4nf))  # Debería imprimir True
```

    True

```python
fd = FunctionalDependency("{A} -> {B}")

mfd = MultivaluedDependency("{B} ->-> {C}")

relvar_not_4nf = Relvar(
    {"A", "B", "C"},
    functional_dependencies={fd},
    multivalued_dependencies={mfd}
)

print(is_relvar_in_4nf(relvar_not_4nf))  # Debería imprimir False
```

    False

```python
mvd1 = MultivaluedDependency("{EmpleadoID} ->-> {Proyecto}")

mvd2 = MultivaluedDependency("{EmpleadoID} ->-> {Habilidad}")

relvar_only_mvd = Relvar(
    {"EmpleadoID", "Proyecto", "Habilidad"},
    multivalued_dependencies={mvd1, mvd2}
)

print(is_relvar_in_4nf(relvar_only_mvd))  # Debería imprimir False
```

    False
