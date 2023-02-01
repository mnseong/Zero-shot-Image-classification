from ZeroShotClassification import ZeroShotImageClassification

zsic = ZeroShotImageClassification()


#Predictions
pred1 = zsic(image="http://images.cocodataset.org/val2017/000000039769.jpg",
            candidate_labels=["birds", "lions", "cats","dogs"],
            )

pred2 = zsic(image="assets/lionandwoman.png",
             candidate_labels=["lions", "humans"],
             )

print(pred1)
print(pred2)