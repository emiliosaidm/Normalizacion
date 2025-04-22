from .components import FunctionalDependency, Attribute, Relvar

def closure(attributes: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> set[Attribute]:
    finished = False
    while not finished:
        initial = len(attributes)
        for fd in functional_dependencies:
            if fd.determinant.issubset(attributes):
                attributes = attributes.union(fd.dependant)
        if initial == len(attributes):
            finished = True

    return attributes

def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    closure_set = closure(
        attributes=attributes,
        functional_dependencies=functional_dependencies
    )
    return heading.issubset(closure_set)

def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    is_spk = is_superkey(
        attributes=attributes,
        heading=heading,
        functional_dependencies=functional_dependencies
    )
    if not is_spk:
        return False

    for attr in attributes:
        aux = attributes - {attr}
        if is_superkey(aux, heading, functional_dependencies):
            return False

    return True


def is_relvar_in_bcnf(relvar: Relvar):
    non_trivial_fd = {fd for fd in relvar.functional_dependencies if not fd.is_trivial()}

    for fd in non_trivial_fd:
        if not is_superkey(
            fd.determinant,
            relvar.heading,
            relvar.functional_dependencies
        ):
            return False

    return True

def is_relvar_in_4nf(relvar: Relvar):
    non_trivial_mfd = {mfd for mfd in relvar.multivalued_dependencies if not mfd.is_trivial(relvar.heading)}

    for mfd in non_trivial_mfd:
        if not is_superkey(
            mfd.determinant,
            relvar.heading,
            relvar.functional_dependencies
        ):
            return False

    return True
