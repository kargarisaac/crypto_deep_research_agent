###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Any, Dict, List, Optional, TypeVar, Union, TypedDict, Type, Literal, cast
from typing_extensions import NotRequired
import pprint

import baml_py
from pydantic import BaseModel, ValidationError, create_model

from . import partial_types, types
from .types import Checked, Check
from .type_builder import TypeBuilder
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME
from .sync_request import HttpRequest, HttpStreamRequest
from .parser import LlmResponseParser, LlmStreamParser

OutputType = TypeVar('OutputType')


# Define the TypedDict with optional parameters having default values
class BamlCallOptions(TypedDict, total=False):
    tb: NotRequired[TypeBuilder]
    client_registry: NotRequired[baml_py.baml_py.ClientRegistry]
    collector: NotRequired[Union[baml_py.baml_py.Collector, List[baml_py.baml_py.Collector]]]


class BamlSyncClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __stream_client: "BamlStreamClient"
    __http_request: "HttpRequest"
    __http_stream_request: "HttpStreamRequest"
    __llm_response_parser: LlmResponseParser
    __baml_options: BamlCallOptions

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager, baml_options: Optional[BamlCallOptions] = None):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__stream_client = BamlStreamClient(self.__runtime, self.__ctx_manager, baml_options)
      self.__http_request = HttpRequest(self.__runtime, self.__ctx_manager)
      self.__http_stream_request = HttpStreamRequest(self.__runtime, self.__ctx_manager)
      self.__llm_response_parser = LlmResponseParser(self.__runtime, self.__ctx_manager)
      self.__llm_stream_parser = LlmStreamParser(self.__runtime, self.__ctx_manager)
      self.__baml_options = baml_options or {}

    @property
    def stream(self):
      return self.__stream_client

    @property
    def request(self):
      return self.__http_request

    @property
    def stream_request(self):
      return self.__http_stream_request

    @property
    def parse(self):
      return self.__llm_response_parser

    @property
    def parse_stream(self):
      return self.__llm_stream_parser

    def with_options(
      self,
      tb: Optional[TypeBuilder] = None,
      client_registry: Optional[baml_py.baml_py.ClientRegistry] = None,
      collector: Optional[Union[baml_py.baml_py.Collector, List[baml_py.baml_py.Collector]]] = None,
    ) -> "BamlSyncClient":
      """
      Returns a new instance of BamlSyncClient with explicitly typed baml options
      for Python 3.8 compatibility.
      """
      new_options: BamlCallOptions = self.__baml_options.copy()

      # Override if any keyword arguments were provided.
      if tb is not None:
          new_options["tb"] = tb
      if client_registry is not None:
          new_options["client_registry"] = client_registry
      if collector is not None:
          new_options["collector"] = collector
      return BamlSyncClient(self.__runtime, self.__ctx_manager, new_options)

    
    def AnswerQuestion(
        self,
        question: str,context: List[types.ContextItem],
        baml_options: BamlCallOptions = {},
    ) -> types.Answer:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "AnswerQuestion",
        {
          "question": question,"context": context,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(types.Answer, raw.cast_to(types, types, partial_types, False))
    
    def AnswerQuestionWithContext(
        self,
        question: str,context: str,
        baml_options: BamlCallOptions = {},
    ) -> str:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "AnswerQuestionWithContext",
        {
          "question": question,"context": context,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(str, raw.cast_to(types, types, partial_types, False))
    
    def ClarifyQuestion(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> types.Clarification:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "ClarifyQuestion",
        {
          "question": question,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(types.Clarification, raw.cast_to(types, types, partial_types, False))
    
    def CritiqueAnswer(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> types.Critique:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "CritiqueAnswer",
        {
          "question": question,"answer": answer,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(types.Critique, raw.cast_to(types, types, partial_types, False))
    
    def DecomposeQuestion(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> types.SubQuestions:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "DecomposeQuestion",
        {
          "question": question,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(types.SubQuestions, raw.cast_to(types, types, partial_types, False))
    
    def GenerateSubqueries(
        self,
        question: str,clarification_details: str,
        baml_options: BamlCallOptions = {},
    ) -> List[str]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "GenerateSubqueries",
        {
          "question": question,"clarification_details": clarification_details,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(List[str], raw.cast_to(types, types, partial_types, False))
    
    def PlanSteps(
        self,
        question: str,subqueries: List[str],
        baml_options: BamlCallOptions = {},
    ) -> types.Plan:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "PlanSteps",
        {
          "question": question,"subqueries": subqueries,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(types.Plan, raw.cast_to(types, types, partial_types, False))
    
    def RankResults(
        self,
        question: str,subqueries: List[str],results: List[types.ResultItem],top_k: int,
        baml_options: BamlCallOptions = {},
    ) -> List[types.RankedResultItem]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "RankResults",
        {
          "question": question,"subqueries": subqueries,"results": results,"top_k": top_k,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(List[types.RankedResultItem], raw.cast_to(types, types, partial_types, False))
    
    def RewriteQuery(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> str:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "RewriteQuery",
        {
          "question": question,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(str, raw.cast_to(types, types, partial_types, False))
    
    def SynthesizeAnswers(
        self,
        question: str,sub_answers: List[str],
        baml_options: BamlCallOptions = {},
    ) -> str:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.call_function_sync(
        "SynthesizeAnswers",
        {
          "question": question,"sub_answers": sub_answers,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )
      return cast(str, raw.cast_to(types, types, partial_types, False))
    



class BamlStreamClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __baml_options: BamlCallOptions
    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager, baml_options: Optional[BamlCallOptions] = None):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__baml_options = baml_options or {}

    
    def AnswerQuestion(
        self,
        question: str,context: List[types.ContextItem],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Answer, types.Answer]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "AnswerQuestion",
        {
          "question": question,
          "context": context,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[partial_types.Answer, types.Answer](
        raw,
        lambda x: cast(partial_types.Answer, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.Answer, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def AnswerQuestionWithContext(
        self,
        question: str,context: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[str], str]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "AnswerQuestionWithContext",
        {
          "question": question,
          "context": context,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[Optional[str], str](
        raw,
        lambda x: cast(Optional[str], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(str, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def ClarifyQuestion(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Clarification, types.Clarification]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "ClarifyQuestion",
        {
          "question": question,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[partial_types.Clarification, types.Clarification](
        raw,
        lambda x: cast(partial_types.Clarification, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.Clarification, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def CritiqueAnswer(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Critique, types.Critique]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "CritiqueAnswer",
        {
          "question": question,
          "answer": answer,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[partial_types.Critique, types.Critique](
        raw,
        lambda x: cast(partial_types.Critique, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.Critique, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def DecomposeQuestion(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.SubQuestions, types.SubQuestions]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "DecomposeQuestion",
        {
          "question": question,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[partial_types.SubQuestions, types.SubQuestions](
        raw,
        lambda x: cast(partial_types.SubQuestions, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.SubQuestions, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def GenerateSubqueries(
        self,
        question: str,clarification_details: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[List[Optional[str]], List[str]]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "GenerateSubqueries",
        {
          "question": question,
          "clarification_details": clarification_details,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[List[Optional[str]], List[str]](
        raw,
        lambda x: cast(List[Optional[str]], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(List[str], x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def PlanSteps(
        self,
        question: str,subqueries: List[str],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Plan, types.Plan]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "PlanSteps",
        {
          "question": question,
          "subqueries": subqueries,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[partial_types.Plan, types.Plan](
        raw,
        lambda x: cast(partial_types.Plan, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.Plan, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def RankResults(
        self,
        question: str,subqueries: List[str],results: List[types.ResultItem],top_k: int,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[List[partial_types.RankedResultItem], List[types.RankedResultItem]]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "RankResults",
        {
          "question": question,
          "subqueries": subqueries,
          "results": results,
          "top_k": top_k,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[List[partial_types.RankedResultItem], List[types.RankedResultItem]](
        raw,
        lambda x: cast(List[partial_types.RankedResultItem], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(List[types.RankedResultItem], x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def RewriteQuery(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[str], str]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "RewriteQuery",
        {
          "question": question,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[Optional[str], str](
        raw,
        lambda x: cast(Optional[str], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(str, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def SynthesizeAnswers(
        self,
        question: str,sub_answers: List[str],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[str], str]:
      options: BamlCallOptions = {**self.__baml_options, **(baml_options or {})}
      __tb__ = options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = options.get("client_registry", None)
      collector = options.get("collector", None)
      collectors = collector if isinstance(collector, list) else [collector] if collector is not None else []

      raw = self.__runtime.stream_function_sync(
        "SynthesizeAnswers",
        {
          "question": question,
          "sub_answers": sub_answers,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
        collectors,
      )

      return baml_py.BamlSyncStream[Optional[str], str](
        raw,
        lambda x: cast(Optional[str], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(str, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    


b = BamlSyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)

__all__ = ["b"]