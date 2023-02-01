from ZeroShotClassification import ZeroShotImageClassification

zsic = ZeroShotImageClassification()


#Predictions
preds = zsic(image="http://images.cocodataset.org/val2017/000000039769.jpg",
            candidate_labels=["birds", "lions", "cats","dogs"],
            )
print(preds)