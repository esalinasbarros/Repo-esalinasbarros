class Pregunta < ApplicationRecord
  belongs_to :producto
  belongs_to :user
  has_many :responses
end
