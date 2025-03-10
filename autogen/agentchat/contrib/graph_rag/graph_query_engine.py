# Copyright (c) 2023 - 2024, Owners of https://github.com/ag2ai
#
# SPDX-License-Identifier: Apache-2.0
#
# Portions derived from https://github.com/microsoft/autogen are under the MIT License.
# SPDX-License-Identifier: MIT
from dataclasses import dataclass, field
from typing import Optional, Protocol

from .document import Document


@dataclass
class GraphStoreQueryResult:
    """A wrapper of graph store query results.

    answer: human readable answer to question/query.
    results: intermediate results to question/query, e.g. node entities.
    """

    answer: Optional[str] = None
    results: list = field(default_factory=list)


class GraphQueryEngine(Protocol):
    """An abstract base class that represents a graph query engine on top of a underlying graph database.

    This interface defines the basic methods for graph-based RAG.
    """

    def init_db(self, input_doc: list[Document] | None = None):
        """This method initializes graph database with the input documents or records.
        Usually, it takes the following steps,
        1. connecting to a graph database.
        2. extract graph nodes, edges based on input data, graph schema and etc.
        3. build indexes etc.

        Args:
        input_doc: a list of input documents that are used to build the graph in database.

        """
        pass

    def add_records(self, new_records: list) -> bool:
        """Add new records to the underlying database and add to the graph if required."""
        pass

    def query(self, question: str, n_results: int = 1, **kwargs) -> GraphStoreQueryResult:
        """This method transform a string format question into database query and return the result."""
        pass
