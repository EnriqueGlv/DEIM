from deimkit import Trainer, Config, configure_dataset

conf = Config.from_model_name("deim_hgnetv2_s")

conf = configure_dataset(
    config=conf,
    image_size=(640, 640),
    train_ann_file="/home/dnth/Desktop/DEIMKit/dataset_collections/leaf_stomata2.v1i.coco/train/_annotations.coco.json",
    train_img_folder="/home/dnth/Desktop/DEIMKit/dataset_collections/leaf_stomata2.v1i.coco/train",
    val_ann_file="/home/dnth/Desktop/DEIMKit/dataset_collections/leaf_stomata2.v1i.coco/valid/_annotations.coco.json",
    val_img_folder="/home/dnth/Desktop/DEIMKit/dataset_collections/leaf_stomata2.v1i.coco/valid",
    train_batch_size=4,
    val_batch_size=4,
    num_classes=3,
    output_dir="./outputs/leaf-stomata/deim_hgnetv2_s_50ep_640px",
)


trainer = Trainer(conf)

trainer.fit(epochs=50, save_best_only=True)
