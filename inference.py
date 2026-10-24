
import torch
def predicted_image(model, image_tensor, class_mapping):
  model.eval()
  device = next(model.parameters()).device

  with torch.no_grad():
    image_batch = image_tensor.unsqueeze(0).to(device)
    # add batch dimension and move image to device

    #run the model and select the class id 
    scores = model(image_batch)
    predicted_class = scores.argmax(dim = 1).item()

  #convert class id to string and to class_name
  class_id = str(predicted_class)
  class_name = class_mapping[str(predicted_class)]

  return{
      "class_id" : predicted_class,
      "class_name" : class_name
  }
