from .expectation import (log_dirichlet_expectation,
                          stick_expectation)

from .fast_expectation import log_stick_expectation
#from .extmath import log_normalize_row_exp

from .sample_generator import (make_doc_word_matrix,
                               make_uniform_doc_word_matrix)

__all__ = [
    'log_dirichlet_expectation',
    'log_stick_expectation',
#    'log_normalize_row_exp',
    'stick_expectation',
    'make_doc_word_matrix',
    'make_uniform_doc_word_matrix'
]
