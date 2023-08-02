class AddUserToPregunta < ActiveRecord::Migration[7.0]
  def change
    add_reference :pregunta, :user, null: false, foreign_key: true
  end
end
