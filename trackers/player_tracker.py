from ultralytics import YOLO

class PlayerTracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
    
    # detect players in a list of frames
    def detect_frames(self, frames):
        player_detections = []
        for frame in frames:
            player_dict = self.detect_frame(frame)
            player_detections.append(player_dict)
        return player_detections

    # detect players in a single frame
    def detect_frame(self, frame):
        # track, persist means that the model will use the same set of weights for the next frame
        results = self.model.track(frame, persist=True)
        id_name_dict = results.names

        player_dict = {}
        for box in results.boxes:
            track_id = box.id
            result = box.xyxy.tolist()[0]
            object_cls_id = box.cls.tolist()[0]
            object_cls_name = id_name_dict[object_cls_id]
            # only consider players, ignore other objects
            if object_cls_name == "person":
                player_dict[track_id] = result
        return player_dict
    
    def track_players(self, frames):
        player_dict = {}
        for frame in frames:
            player_dict = self.detect_frame(frame)
            