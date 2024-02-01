import { http } from "@/utils/http";

type encoderData = {
  id: string;
  number: string;
  ip: string;
  time: string;
  length: string;
  type: string;
  path: string;
};

export const getAllEncoderData = () => {
  return http.request<any>("get", "/api/encoder_data/get_all_encoder_data");
};
export const showVoice = (data) => {
  return http.request("post", "/api/data/show_voice", {data});
};

export const saveEncoderData = (data) => {
  return http.request("post", "/api/encoder_data/save_encoder_data", {data});
};

