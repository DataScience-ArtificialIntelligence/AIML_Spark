import gc

def empty_vram(model, pipe, trainer):
    del model
    del pipe
    del trainer
    gc.collect()
    gc.collect()