# Define critical settings and/or override defaults specified in
# settings.py. Copy this file to settings_local.py in the same
# directory as settings.py and edit. Any settings defined here
# will override those defined in settings.py



# Set this to point to your compiled checkout of caffe
caffevis_caffe_root      = '/path/to/caffe'

# Load model: caffenet-yos
# Path to caffe deploy prototxt file. Minibatch size should be 1.
caffevis_deploy_prototxt = '%DVT_ROOT%/models/caffenet-yos/caffenet-yos-deploy.prototxt'

# Path to network weights to load.
torchvis_network_weights = 'IMAGENET1K_V1'
torchvis_network = 'alexnet'

# Other optional settings; see complete documentation for each in settings.py.
torchvis_data_mean       = '%DVT_ROOT%/models/caffenet-yos/ilsvrc_2012_mean.npy'
torchvis_labels          = '%DVT_ROOT%/models/caffenet-yos/ilsvrc_2012_labels.txt'
torchvis_label_layers    = ('fc8', 'prob')
torchvis_prob_layer      = 'prob'
torchvis_unit_jpg_dir    = '%DVT_ROOT%/models/caffenet-yos/unit_jpg_vis'
torchvis_jpgvis_layers   = ['conv1', 'conv2', 'conv3', 'conv4', 'conv5', 'fc6', 'fc7', 'fc8', 'prob']
torchvis_jpgvis_remap    = {'pool1': 'conv1', 'pool2': 'conv2', 'pool5': 'conv5'}
def caffevis_layer_pretty_name_fn(name):
    return name.replace('pool','p').replace('norm','n')

# Use GPU? Default is True.
#caffevis_mode_gpu = True
# Display tweaks.
# Scale all window panes in UI by this factor
#global_scale = 1.0
# Scale all fonts by this factor    
#global_font_size = 1.0
