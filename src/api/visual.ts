import { http } from "@/utils/http";

export const getEncoderErrorData = (data) => {
  return http.request("post", "/api/visual/get_encoder_error_data", {data});
};