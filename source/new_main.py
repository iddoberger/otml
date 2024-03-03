import codecs
import logging

from otml_configuration_manager import OtmlConfigurationManager
from pathlib import Path


current_file_path = Path(__file__)
source_directory_path = current_file_path.parent
fixtures_directory_path = Path(source_directory_path, "tests", "fixtures")


configuration_file_path = str(Path(fixtures_directory_path, "configuration", "otml_configuration.json"))

configuration_json_str = codecs.open(configuration_file_path, 'r').read()
OtmlConfigurationManager(configuration_json_str)

from grammar.lexicon import Lexicon
from grammar.feature_table import FeatureTable
from grammar.constraint_set import ConstraintSet
from grammar.grammar import Grammar
from traversable_grammar_hypothesis import TraversableGrammarHypothesis
from corpus import Corpus
from simulated_annealing import SimulatedAnnealing



logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s', "%Y-%m-%d %H:%M:%S")
file_log_handler = logging.FileHandler("my.log", mode='w')
file_log_handler.setFormatter(file_log_formatter)
logger.addHandler(file_log_handler)


feature_table_file_path = str(Path(fixtures_directory_path, "feature_table", "french_deletion_feature_table.json"))
corpus_file_path = str(Path(fixtures_directory_path, "corpora", "french_deletion_corpus.txt"))
constraint_set_file_path = str(Path(fixtures_directory_path, "constraint_sets", "french_deletion_constraint_set.json"))


configuration_json_str = codecs.open(configuration_file_path, 'r').read()
OtmlConfigurationManager(configuration_json_str)


feature_table = FeatureTable.load(feature_table_file_path)
corpus = Corpus.load(corpus_file_path)
constraint_set = ConstraintSet.load(constraint_set_file_path, feature_table)
lexicon = Lexicon(corpus.get_words(), feature_table)
grammar = Grammar(feature_table, constraint_set, lexicon)
data = corpus.get_words()
traversable_hypothesis = TraversableGrammarHypothesis(grammar, data)
simulated_annealing = SimulatedAnnealing(traversable_hypothesis)
simulated_annealing.run()
