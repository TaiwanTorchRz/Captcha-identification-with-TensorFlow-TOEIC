	u�V.#@u�V.#@!u�V.#@	��}&,��?��}&,��?!��}&,��?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$u�V.#@7�A`�в?AK�=��"@Y�HP��?*	�����I@2f
/Iterator::Model::Prefetch::MapAndBatch::Shuffle��6��?!���J@)��6��?1���J@:Preprocessing2F
Iterator::ModelL7�A`�?!jH�+o@@)�j+��݃?1w�V�R3@:Preprocessing2P
Iterator::Model::Prefetch_�Q�{?!ZEtJu+@)_�Q�{?1ZEtJu+@:Preprocessing2]
&Iterator::Model::Prefetch::MapAndBatchF%u�{?!PC�^yK*@)F%u�{?1PC�^yK*@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.4% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	7�A`�в?7�A`�в?!7�A`�в?      ��!       "      ��!       *      ��!       2	K�=��"@K�=��"@!K�=��"@:      ��!       B      ��!       J	�HP��?�HP��?!�HP��?R      ��!       Z	�HP��?�HP��?!�HP��?JCPU_ONLY